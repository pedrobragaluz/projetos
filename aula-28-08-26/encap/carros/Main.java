public class Main{
    public static void main(String[] args) {
        Carros c = new Carros();
        c.setModelo("Honda");
        String carro = c.geModelo();
        c.setano(2000);
        int ano = c.getAno();
        c.setMarca("Civic");
        String marca = c.getMarca();
        c.setVelocidade(200);
        float velo = c.getVelocidade();

        System.out.println("O Modelo do Carro é " + carro);
        System.out.println("O ano do carro é " + ano);
        System.out.println("A Marca do Carro é " + marca);
        System.out.println("A velocidade do carro é a "  + velo + "KM/h");

    }
}