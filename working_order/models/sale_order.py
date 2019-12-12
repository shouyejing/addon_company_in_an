# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class sale_order(models.Model):
    _inherit = "sale.order"

    coupon_code = fields.Char('Coupon Code')
    # orther information
    payment_method = fields.Char('Payment Method')
    order_date = fields.Datetime('Order Date')
    transaction_id = fields.Char('Transaction ID')
    order_ip = fields.Char('Order IP')
    tracking_number = fields.Char('Tracking Number')
    order_shipping_location = fields.Char('Order Shipping Location')
    #
    store_id = fields.Many2one('store.info', string='Store')
    market_place_id = fields.Many2one('market.place', string='Market Place')
    # delivery_method_id = fields.Many2one('delivery.method', string='Delivery Method') # remove
    platform_id = fields.Many2one('platform.list', string='Platform')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Confirm Sale'),
        ('paid', 'Paid'),
        ('product hold', 'Product Hold'),
        ('in product', 'In Product'),
        ('to delivery', 'To Delivery'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


class ir_attachment(models.Model):
    _inherit = "ir.attachment"
    sale_order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')


class sale_order_line(models.Model):
    _inherit = "sale.order.line"

    attachment_ids = fields.One2many('ir.attachment', 'sale_order_line_id',
                                     string='Attachments')
    check_product_id = fields.Many2one('check.product', string='check product')
    check_maped = fields.Boolean(string='Map Check Product', default=False)
    description = fields.Char('Description')

    @api.multi
    def btn_img(self):
        view_id = self.env.ref('working_order.view_sale_order_line_imgae_from', False)
        return {
            'name': _('Image From'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.order.line',
            'view_id': view_id.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
