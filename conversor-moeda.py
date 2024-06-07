taxa_brl_para_usd = 5.29 # 1 USD + 5.29 BRL 
taxa_usd_para_brl = 1 / taxa_brl_para_usd # 1 brl = 0.20 USD 

while True: 
    #exibe o menu de opções 
    print("\n escolha uma opção:")
    print("1.BRL para US$:")
    print("2.US$ para BRL") 
    print("3.sair")

    opção = input("digite o número da opção desejada")
    if opção == '1':
        valor_brl = float(input("digite o valor em (R$)"))
        valor_usd = valor_brl / taxa_brl_para_usd
        print(f"R${valor_brl:.2f} é equivalente a US$ {valor_usd:.2f}")
    elif opção == '2':
        valor_usd = float (input("digite o valor em dólares(US$)"))
        valor_brl1 = valor_usd * taxa_brl_para_usd
        print(f"US$ {valor_usd:.2f} é equivalente a R$ {valor_brl1:.2f}")
    elif opção == '3':
        print("saindo...")
        break
    else:
        print("opção inválida..tente novamente.")
        