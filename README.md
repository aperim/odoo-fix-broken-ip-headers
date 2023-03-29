
# Odoo Fix Real User IP Address

Odoo's support for proxying and/or load balancing is broken, this add-on is a temporary fix while we wait for Odoo to [fix this critical issue](https://github.com/odoo/odoo/issues/104947) with the platform.

## Description

Odoo is incorrectly configured to handle an instance behind a load balancer or proxy. This Odoo addon looks for the presence of a `X-Forwarded-For` header and sets both the `HTTP_X_FORWARDED_FOR` and `REMOTE_ADDR` environ variables to allow Odoo to correctly parse and store the users real remote IP address.

## Getting Started

### DANGER

This addon blindly accepts the `X-Forwarded-For` header making the bold assumption that you know what you are doing. If you don't know why this is dangerous, please don't move forward and install this addon until you have an understanding of header forgery and ways to mitigate it.

In a nutshell, **the installation of this addon, in an incorrectly configured environment can and will lead to potentially disastrous security outcomes**.

### Addons Folder

* You must have your addon location configured either in Odoo's configuration files or with the [--addons-path](https://www.odoo.com/documentation/16.0/developer/reference/cli.html#cmdoption-odoo-bin-addons-path) command line parameter.
* You must be able to add folders to that location

### Installing

* Copy all the files from this repository into a folder called `fix-ip` in your addons folder. (example below)
* In Odoo as an administrator
	* Activate the [developer mode](https://www.odoo.com/documentation/16.0/applications/general/developer_mode.html#developer-mode).
	* In the apps menu, click the _Update Apps List_ button.
	* In the dialog that appears, click the _Update_ button.
	* Remove "App" from the search bar, and search for "fix"
	* <img width="567" alt="search_for_fix" src="https://user-images.githubusercontent.com/4564803/228408528-b51b980a-c088-4100-921c-ffb745622408.png">
	* Activate the fix-ip addon

### Addon File Installation Example

```bash
cd /mnt/extra-addons
curl -L https://github.com/aperim/odoo-fix-broken-ip-headers/archive/refs/heads/main.zip -o fix-ip.zip
unzip -d fix-ip fix-ip.zip && f=(fix-ip/*) && mv fix-ip/*/* fix-ip && rm -Rf "${f[@]}"
rm fix-ip.zip
```

or

```bash
cd /mnt/extra-addons
mkdir fix-ip
curl -L https://github.com/aperim/odoo-fix-broken-ip-headers/tarball/master -o fix-ip.tgz
tar zxvf fix-ip.tgz --directory fix-ip --strip-components=1
rm -Rf fix-ip.tgz
```

## Help

Create an issue with logs.

## Authors

[@troykelly](https://github.com/troykelly) - Odoo addon for installation with instructions
[@andreabak](https://github.com/andreabak) - Initial code sample for addon

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details

## Acknowledgments

Issue identification and discussion
* [@netfxtech](https://github.com/netfxtech)
* [@pmig](https://github.com/pmig)
