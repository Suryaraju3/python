def t_shope():
    print("----------ABC T-shirt shope--------")
    
    print("---------Welcome to ABC shope---------")
    
    print('''             1.puma 
             2.Levi's ''')
    print("---choose only number---")
    choose=int(input("Choose your brand: "))
    p=1
    l=2
    if choose == p :
        puma()
    elif choose == l:
        levis()
    elif choose !=p:
        print("choose correctly on the brand")
    elif choose != p:
        print("choose correctly on the brand")
    else:
        print("Verify them all.")
t_shope()


def puma():
    print("We have 3 t-shirts; choose what you want: ")
    #T-shirts price,discount_price,maximum retail price
    pb=1
    priceA=1754  #t-price
    mA=2699      # Maximum Retail Price
    mad=35       #Discount
    
    pb2=2       
    priceB=539   #t-price
    mB=599       #Maximum Retail Price
    mad2=10      #Discount
    
    
    pb3=3       
    priceC=419   #t-price
    mC=419       #Maximum Retail Price
    mad2=10      #Discount
    
    buy=int(input("Click on the t-shirts: ")) 
    if buy == pb:
        print(f"₹{priceA} Price Details Maximum Retail PriceRs. {mA} Discount{mad}% OFF Selling PriceRs. {priceA} (Incl. of all taxes) MRP ₹({mad}% OFF)")
    elif buy == pb2:
        print(f" ₹{priceB} Price Details Maximum Retail PriceRs. {mB} (Incl. of all taxes) Discount{  mad2}% OFF Selling PriceRs. {priceB} (Incl. of all taxes) MRP ₹599({mad2}% OFF)")
    elif buy == pb3:
        print(f" ₹ {priceC} Price Details Maximum Retail PriceRs. {mC} (Incl. of all taxes) Discount Selling PriceRs. {priceC} (Incl. of all taxes)")
    else:
        print("verify the all")   
puma()


def levis():
    
    print("We have 3 t-shirts; choose what you want: ")
#t-shire brand and count 3

    lb=1
    lpriceA=361  #t-price
    lmA=380      # Maximum Retail Price
    lmad=5       #Discount
    
    lb2=2       
    lpriceB=1439   #t-price
    lmB=1799      #Maximum Retail Price
    lmad2=20      #Discount
    #================= 
    lb3=3       
    lpriceC=5499   #t-price
    lmC=5499       #Maximum Retail Price
    lmad2=10      #Discount

    buyl=int(input("Click on the t-shirts: "))
    if buyl == lb:
        print(f"₹{lpriceA} Price Details Maximum Retail PriceRs. {lmA} Discount{lmad}% OFF Selling PriceRs. {lpriceA} (Incl. of all taxes) MRP ₹({lmad}% OFF)")
    elif buyl == lb2:
        print(f"₹{lpriceB} Price Details Maximum Retail PriceRs. {lmB} (Incl. of all taxes) Discount{  lmad2}% OFF Selling PriceRs. {lpriceB} (Incl. of all taxes) MRP ₹599({lmad2}% OFF)")
    elif buyl == lb3:
        print(f"₹ {lpriceC} Price Details Maximum Retail PriceRs. {lmC} (Incl. of all taxes) Discount Selling PriceRs. {lpriceC} (Incl. of all taxes)")
    else:
        print("Verify them all.")
levis()












