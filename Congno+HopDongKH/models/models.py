from odoo import models, fields, api


class Task1(models.Model):
    _inherit = "res.partner"

    money_description = fields.Char(string='Han Muc Tien No')
    time_description = fields.Char(string='Han Muc Thoi gian No (Thang)')


class Contract(models.Model):
    _name = "contact1234"

    name = fields.Char('name')
    Hop_Dong_Khung = fields.Char('Hop_Dong_Khung')
    Thong_Tin_Hop_Dong = fields.Char('Thong_Tin_Hop_Dong')
    Sale_Order = fields.Many2one("sale.order")
    Customer_ID = fields.Many2one("res.partner", related="Sale_Order.partner_id")
    Dia_Chi_Hop_Dong = fields.Char('Dia_Chi_Hop_Dong')
    Ma_Hop_Dong = fields.Char('Ma_Hop_Dong')
    So_CCCD = fields.Char('So_CCCD')
    Ngay_Cap = fields.Date('Ngay_Cap', required=False)
    Noi_Cap = fields.Char('Noi_Cap')
    Dia_Chi_Giao_Hang = fields.Char('Dia_Chi_Giao_Hang')
    Loai_Hop_Dong = fields.Char('Loai_Hop_Dong')
    Ngay_Ky_Hop_Dong = fields.Date('Ngay_Ky_Hop_Dong', required=False)
    Nguoi_Ky = fields.Char('Nguoi_Ky')
    Chuc_Vu = fields.Char('Chuc_Vu')
    Ngay_Thi_Cong_Hop_Dong = fields.Datetime('Ngay_Thi_Cong_Hop_Dong', required=False)
    Ngay_Ket_Thuc_Hop_Dong = fields.Datetime('Ngay_Ket_Thuc_Hop_Dong', required=False)
    Hang_Muc_Hop_Dong = fields.Char('Hang_Muc_Hop_Dong')
    Amount_Total = fields.Char('Amount_Total')
    Tien_Do_Hop_Dong = fields.Char('Tien_Do_Hop_Dong')
    Ngay_Con_Lai = fields.Date('Ngay_Con_Lai', required=False)
    Ngay_Giao_Hang = fields.Datetime('Ngay_Giao_Hang', required=False)

    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")

    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id')
    sequence = fields.Char(string="Sequence", default='New')

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'sequence.contract') or 'New'
        result = super(Contract, self).create(vals)
        return result


class Task2(models.Model):
    _inherit = "sale.order"

    Contracts = fields.Many2one("contact1234")
   # ten_hop_dong = fields.Many2one("sequence", related="Contracts.sequence")

    def test(self):
        try:
            form_view_id = self.env.ref("contract.form.view").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'test123',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(form_view_id, 'contract_form_view')],
            'target': 'current',
        }

    def my_button(self):
        return {
            'name': "Your String",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'contact1234',
            "context": {"default_Sale_Order": self.id},
            'view_id': self.env.ref('test_anh.contract_form_view').id,
            'target': 'current',
        }


