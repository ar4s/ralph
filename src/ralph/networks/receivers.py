from ralph.dns.dnsaas import DNSaaS


def send_ipaddress_to_dnsaas(instance, created, *args, **kwargs):
    keys = ['address', 'hostname']
    data_to_send = {
        key: {
            'old': instance._previous_state[key],
            'new': instance.__dict__[key]
        }
        for key in keys
        # if instance._previous_state[key] != instance.__dict__[key]
    }
    if data_to_send:
        data_to_send['action'] = 'add' if created else 'update'
        data_to_send['ip'] = instance._previous_state['address']
        DNSaaS().send_ipaddress_data(data_to_send)
