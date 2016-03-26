@echo off
set path=C:\Program Files\wkhtmltopdf\bin;%path%
python odoo.py --config .openerp-server.config --data-dir=DATA_DIR --xmlrpc-port=8008 --log-level=debug
