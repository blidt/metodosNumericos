public strictfp class Suma {

    public static void main(String[] args) {
    Double resultadod = 0.0;
    Float resultadof = 0.0f;       
        for(int i = 1; i < 5001; i++) {
            resultadof = resultadof + 1/(i*i); 
        }
        System.out.println("El resultado sumando de izquierda a derecha con precision sencilla es " + resultadof);
        System.out.println("\n");
        System.out.println("-------------------------------------------------");
        resultadof = 0.0f;
        for(int i = 5000; i > 0; i--) {
            resultadof = resultadof + 1/(i*i);
        }
        System.out.println("El resultado sumando de derecha a izquerda con precision sencilla es " + resultadof);
        System.out.println("\n");
        System.out.println("-------------------------------------------------");


        for(int i = 1; i < 5001; i++) {
            resultadod = resultadod + 1/(i*i);
        }
        System.out.println("El resultado sumando de izquierda a derecha con precision doble es " + resultadod);
        System.out.println("\n");
        System.out.println("-------------------------------------------------");
        resultadod = 0.0;
        for(int i = 5000; i > 0; i--) {
            resultadod = resultadod + 1/(i*i);
        }
        System.out.println("El resultado sumando de derecha a izquerda con precision doble es " + resultadod);
        System.out.println("\n");
        System.out.println("-------------------------------------------------");

    }    
        
}