public strictfp class Bisección {

    public static void main(String[] args) {
        print "\nIngrese el numero: "
        numero = System.in.newReader().readLine() as Double
        if(numero < 0){
            break
        }
        resultado =  Math.sqrt(Math.pow(numero,2))
        print "El resultado es: " + resultado
        resultado = Math.sqrt(Math.pow(numero,2)) - numero
        print "\nEl resultado es: " + resultado
    }
    
    }    
        
}