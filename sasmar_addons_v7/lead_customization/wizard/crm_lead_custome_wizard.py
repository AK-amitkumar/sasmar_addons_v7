from openerp.osv import fields, osv
from openerp.tools.translate import _

class crm_lead_custome_wizard(osv.osv_memory):
	_name = "crm.lead.custome.wizard"
	_columns={
    }

	def create_customer(self,cr, uid, ids, context=None):
		crm_lead_obj = self.pool.get('crm.lead')
		customer_obj = self.pool.get('res.partner')
		values = {}
		if context.get('active_ids',False):
			crm_obj = crm_lead_obj.browse(cr, uid, context['active_ids'])
			for crm_obj in crm_lead_obj.browse(cr, uid, context['active_ids']):
				if crm_obj.partner_id:
					raise osv.except_osv(_('Warning'), _('You cannot create Customer who is already created.'))
				if not crm_obj.partner_id:
					values = {
						'name': crm_obj.contact_name or '',
						'street': crm_obj.street or '',
						'city': crm_obj.city or '',
						'state_id': crm_obj.state_id.id or '',
						'zip': crm_obj.zip or '',
						'country_id': crm_obj.country_id.id or '',
						'user_id': crm_obj.user_id.id or '',
						'customer': True,
						'email': crm_obj.email_from or '',
						'phone': crm_obj.phone or '',
						'mobile': crm_obj.mobile or '',
						'fax': crm_obj.fax or '',
						'title': crm_obj.title.id or '',
						'website': crm_obj.website or '',
					}
					cust_id = customer_obj.create(cr, uid, values)
					crm_lead_obj.write(cr, uid, crm_obj.id, {'partner_id': cust_id}, context=context)
			return True
