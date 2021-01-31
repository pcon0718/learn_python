def make_car(make, model, **car_info):
    car_info['car_make'] = make
    car_info['car_model'] = model
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)