import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server2 extends Thread {
	private Socket concurrentSocket;

	public server2(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server2 client = new server2(clientSocket);
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

                float idade = Integer.parseInt(dados[2]);
                char c = dados[1].charAt(0);

				if(idade >= 18 && (c == 'M' || c == 'O')){
					msg = new String("Maioridade atingida");
				}
				else if(idade == 21 && c == 'F'){
					msg = new String("Maioridade atingida");
				}
                else
                    msg = new String("Maioridade nao atingida");
                    
                out.println(msg);
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}