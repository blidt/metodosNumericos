public strictfp class algoriitmoTarea2 {

    public static void main(String[] args) {
    Double numero = 0.01
    Double resultado = 0.0
    
    while(numero > 0){
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