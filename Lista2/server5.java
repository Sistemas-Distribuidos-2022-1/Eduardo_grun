import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server5 extends Thread {
	private Socket concurrentSocket;

	public server5(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server5 client = new server5(clientSocket);
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

                age = Integer.parseInt(dados[0]);

                if (age >= 5 && age <= 7)
                    msg = "Infantil A";
                else if (age >= 8 && age <= 10)
                    msg = "Infantil B";
                else if (age >= 11 && age <= 13)
                    msg = "Juvenil A";
                else if (age >= 14 &&  age <= 17)
                    msg = "Juvenil B";
                else if (age >= 18)
                    msg = "Adulto";
                else
                    msg = "Idade invalida";
            
                out.println(msg);
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}