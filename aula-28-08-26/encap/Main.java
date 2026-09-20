public class Main{
    public static void main(String[] args) {
        Aluno a = new Aluno();
        String matri = a.getMatricula();
        a.setMatricula("2059");
        String nome = a.getNome();
        a.setNome("Pedro");

        System.out.println("O nome do aluno é "  + nome + "a matrícula é " +  matri);
    }
}