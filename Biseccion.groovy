import java.math.BigDecimal

public strictfp class Biseccion {

    public static void main(String[] args) {
        BigDecimal a
        BigDecimal b
        BigDecimal tolerancia
        BigDecimal x
        BigDecimal resultado = 1
        print "\nIngrese el valor de a: "
        a = System.in.newReader().readLine() as BigDecimal
        print "\nIngrese el valor de b: "
        b = System.in.newReader().readLine() as BigDecimal
        print "\nIngrese la tolerancia: "
        tolerancia = System.in.newReader().readLine() as BigDecimal

        while((b-a)>tolerancia){
            x = ((a+b)/2)
            println "La mitad del intervalo está en " + x
            resultado = funcion(x)
            println "\nx_k= " + x
            println "\na_k=  " + a
            println "\nb_k=  " + b
            println "\nf(x_k)=  " + resultado
            if(funcion(a)*resultado<0){
                b=x
            }else{
                a=x
            }
        }

    }

    private static BigDecimal funcion(BigDecimal x){
        250*((Math.pow((1 + (x/12)),36)-1)/(x/12)) + 13500*(Math.pow((1+(x/12)),36))-25000
    }

}