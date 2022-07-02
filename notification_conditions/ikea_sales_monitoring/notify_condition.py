from notification_conditions.ikea_sales_monitoring.url_checks import check_main_url


def need_to_notify(**kwargs) -> bool:
    notification_flag = check_main_url(**kwargs)
    return notification_flag

