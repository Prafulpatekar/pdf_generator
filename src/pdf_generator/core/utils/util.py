from pdf_generator.schemas.users import radio_options

def get_other_text(check_box_activities):
    for check_box in check_box_activities:
        if check_box not in ["reading", "walking", "music"]:
            return check_box
    return None

def process_form_data(form_data):
    processed_data = {}
    if 'check_box_activities' in form_data:
        check_box_values = [value for value in form_data.getlist('check_box_activities')]
        processed_data['check_box_activities'] = check_box_values
    else:
        processed_data['check_box_activities'] = []

    for key, value in form_data.items():
        if key != 'check_box_activities':
            processed_data[key] = value
    return processed_data

def generate_dict_data(new_user,date_obj,check_box_activities,radio_activities):
    return {
            "id": new_user.id,
            "name": new_user.name,
            "month":  date_obj.strftime('%b'),  # Month
            "date": date_obj.strftime('%d')[1:] if date_obj.strftime('%d').startswith('0') else date_obj.strftime('%d'),   # Day of the month
            "year": date_obj.strftime('%Y'),   # Year
            "address": new_user.address,
            "reading": "Yes" if "reading" in check_box_activities else None,
            "walking": "Yes" if "walking" in check_box_activities else None,
            "music": "Yes" if "music" in check_box_activities else None,
            "other": "Yes" if get_other_text(check_box_activities) else None,
            "other_check": get_other_text(check_box_activities) or "",
            "radio": radio_options[radio_activities] if radio_activities in radio_options.keys() else 3,
            "other_radio": radio_activities if radio_activities not in radio_options.keys() else "",
        }