from test_lib import test,report
getal= 14.99
afronden_op=5

afgerond=round(getal*100/afronden_op)*afronden_op/100
print(f"{afgerond}")
expect_content =15.0
calculated_content = afgerond
name = f' afgerond: {getal} op  {afronden_op} cent'
test(name, expect_content, calculated_content )
report()
