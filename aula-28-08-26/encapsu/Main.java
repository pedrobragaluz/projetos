public class Main {
    public static void main(String[] args) {
        Pessoa p = new Pessoa();
        String nome = p.getNome();
        int idade = p.getIdade();

        p.setNome("Pedro");
        p.setIdade(18);

        System.out.println("O nome do aluno é " + nome + "e a idade dele é " + idade);

    }
}

