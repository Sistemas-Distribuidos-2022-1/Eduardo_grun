import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server7 extends Thread {
	private Socket concurrentSocket;

	public server7(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server7 client = new server7(clientSocket);
					client.start();
				}
			}
		} catch (IOException i){
	}
}
    // dados
    public void run(){
		try {
			InputStream inputStream = concurrentSocket.getInputStream();
            
			try (Scanner scanner = new Scanner(inputStream)) {
				OutputStream outputStream = concurrentSocket.getOutputStream();
				PrintWriter out = new PrintWriter(outputStream, true);
        
                String data = scanner.next();
                String[] dados = data.split("_");
                String msg;
                float age;

                int idade = Integer.parseInt(dados[0]);
                int anos = Integer.parseInt(dados[1]);
            
                if (idade >= 65)
                    msg = "Pode se aposentar";
                else if (anos >= 30)
                    msg = "Pode se aposentar";
                else if (idade >= 60 && anos >= 25)
                    msg = "Pode se aposentar";
                else
                    msg = "Nao pode se aposentar";
            
                out.println(msg);
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}