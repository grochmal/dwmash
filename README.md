README for dwmash


## Description

Performs creation and maintenance of a three phase data warehouse.  The three
phases are a staging area, the warehouse itself, and data marts.  `dwmash`
includes several commands, of which most are not useful in all warehouses.  The
general way to invoke `dwmash` is:

    dwmash [global options] [command] [arguments ...]

Each different `command` runs a distinct module, which has arguments of its
own.


## Installation

The installation will construct a `dwmash` command that will be available at
`/usr/local/bin` or from `~/.local/bin` if installed with `--user`.  The
simplest way to install `dwmash` to run:

    sudo pip install .

Or for the local user:

    pip install --user .

`pip` allows you to install a package in *edit* mode, so you can tweak the code
on the fly.  Use `--editable`:

    sudo pip install --editable .

Or:

    pip install --user --editable .

Remember to update `PATH` with `/usr/local/bin` or `~/.local/bin` to access the
installed command.

`pip` shall deal with the dependencies for `dwmash`.  Yet, if you want to
install the dependencies manually, a list of them follows.  Not all
dependencies are required, but you will need the correct database driver to
work with the database engine of your choice:

*   `sqlachemy 1.1.0` or later
*   `pytz` for timezone support
*   `psycopg2` for Postgres support
*   `mysql-connector-python` or `mysql-python` for MySQL/MariaDB support
*   `cx_oracle` for Oracle support


## Copying

Copyright (C) 2016 Michal Grochmal

This file is part of `dwmash`

`dwmash` is free software; you can redistribute and/or modify all or parts of
it under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3 of the License, or (at your option) any
later version.

`dwmash` is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

The COPYING file contains a copy of the GNU General Public License.  If you
cannot find this file, see <http://www.gnu.org/licenses/>.

