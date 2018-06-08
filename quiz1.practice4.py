
lst_date = [
     '2018.01.05', 
     '2018.01.04', 
     '2018.01.03', 
     '2018.01.02']
lst_dow = [
     '금',
     '목',
     '수',
     '화']
lst_price = [
    2497.52, 
    2466.46, 
    2486.35,
    2479.65]

kospi_price = {}
# kospi_price[lst]

for i in range(len(lst_date)):
    kospi_price[lst_date[i]] = {"dow" : lst_dow[i], "price" : lst_price[i]}

    # print(kospi_price)

for i in range(1, len(lst_date)):
    kospi_price[lst_date[i]]['price_diff'] = lst_price[i] - lst_price[i - 1]

    print(kospi_price)
print("price_diff : %f" % kospi_price["2018.01.05"]["price_diff"])
print("Max Min : %f" % kospi_price["2018.01.05"]["price_diff"])