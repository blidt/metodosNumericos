public strictfp class Suma {

    public static void main(String[] args) {
    Float numerof = 0.000001
    Double numerod = 0.000001
        for(int i = 1; i < 10000; i++) {
            numerof = numerof + 0.000001
            numerod = numerod + 0.000001
        }
    System.out.println("El resultado de sumar 0.000001 10,000 veces con precision sencilla es " + numerof)
    System.out.println("El resultado de sumar 0.000001 10,000 veces con precision doble es " + numerod)
    }    
        
}