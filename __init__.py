# -*- coding: utf-8 -*-

from . import controllers
from . import models

import logging

from odoo import models
from odoo.http import request


_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _pre_dispatch(cls, rule, args):
        # This is a hack to fix real ip detection when multiple hops are added in XFF header (eg. Traefik)
        if "X-Forwarded-For" in request.httprequest.headers:
            real_ip = request.httprequest.headers["X-Forwarded-For"].split(',')[0]
            request.httprequest.environ["HTTP_X_FORWARDED_FOR"] = real_ip
            request.httprequest.environ["REMOTE_ADDR"] = real_ip
            _logger.debug(
                "X-Forwarded-For header found, setting REMOTE_ADDR and HTTP_X_FORWARDED_FOR to %s",
                real_ip,
            )
        return super()._pre_dispatch(rule, args)