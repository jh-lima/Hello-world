def main():
    num=int(input('Digite o número para o qual deseja saber a tabuada: '))
    i=1
    while i<= 10:
        produto=num*i
        print(f'{num} X {i} =', produto)
        i+=1
    print('Fim da tabuada')

  
main()
