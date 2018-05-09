# -*- coding:utf-8 -*-

def events(event_id=None):
	if request.method == "POST":
		body = request.json
		if not isinstance(body, dict):
			return get_error_info(2002)

		aId = d.im.get("aId", None)
		if aId:
			body.update(opUId=d.im['uId'], aId=aId)
		else:
			if body.get('wId'):
				waybill, e = WaybillCtrl.find_one(dict(_id=body['wId'], _key=['aId']))
				if e:
					return get_error_info(e)
				else:
					return get_error_info(1003)

				body.update(opUId=d.im['uId'], aId=waybill['aId'])

		model, e = EventModel.create_one(body)
		if e:
			return get_error_info(e)
		event, e = WaybillCtrl.find_one(dict(_id=event['wId']))
		if e:
			return get_error_info(e)
		waybill, e = WaybillCtrl.find_one(dict(_id=event['wId']))
		if e:
			return get_error_info(e)
		event.update(dict(wCrtAt=waybill['crtAt']))
		return jsonify(event)
	elif request.method == 'GET':
		if event_id:
			params = request.args.to_dict()
			params.update({'_id': event_id})

			query, e = EventModel.find_one(params)
			if e:
				return get_error_info(e)

			event, e = EventModel.find_one(query)
			if e:
				return get_error_info(e)
			return jsonify(event)
		else:
			query, e = EventModel.find(request.args.to_dict())
			if e:
				return get_error_info(e)
			find_events, e = EventCtrl.find(query)
			if e:
				return get_error_info(e)
			return jsonify(find_events)

