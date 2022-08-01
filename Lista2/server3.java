import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server3 extends Thread {
	private Socket concurrentSocket;

	public server3(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server3 client = new server3(clientSocket);
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

                float n1 = Float.parseFloat(dados[0]);
                float n2 = Float.parseFloat(dados[1]);
                float n3 = Float.parseFloat(dados[2]);
                float m = (n1+n2)/2;

                if (m >= 7)
                    msg = "Aprovado!";
                else if (m >= 3 && m < 7)
                    if ((m+n3)/2 >= 5)
                        msg = "Aprovado";
                    else
                        msg = "Reprovado!";
                else
                    msg = "Reprovado!";
            
                out.println(msg);
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}