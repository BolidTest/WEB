#!/bin/bash

create_notify_dir
python3 -m pytest  --device=remote --browser=selenoid --alluredir=allure_users_02 tests/VALIDATION/testUsersKeysValidation.py -k test_user_input_name_user
#python3 -m pytest --device=remote --browser=selenoid --alluredir=allure_users_02 tests/SAVE/testUsersKeysSave.py