import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server4 extends Thread {
	private Socket concurrentSocket;

	public server4(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server4 client = new server4(clientSocket);
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
                float peso;

                float alt = Float.parseFloat(dados[0]);
                char c = dados[1].charAt(0);

                if (c == 'M' || c == 'O')
                    peso = (72.7f * alt) - 58;
                else
                    peso = (62.1f * alt) - 44.7f;
            
            
                out.println(Float.toString(peso));
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}