from test_lib import test,report
from calculate_cilinder_content import calculate_cilinder_content

diameter =8
hight  =5
expect_content =251.3
calculated_content = calculate_cilinder_content(diameter,hight)
name = f'test diameter: {diameter} height: {hight}'
test(name, expect_content, calculated_content )

report()