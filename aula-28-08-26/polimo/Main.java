public class Main {
    public static void main(String[] args) {
        Animal pato = new Pato();
        Animal urso = new Urso();

        pato.nome = "Rivotril";
        urso.nome = "Dorflex";

        pato.emitirsom();
        urso.emitirsom();

    }
}
