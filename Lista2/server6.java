import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class server6 extends Thread {
	private Socket concurrentSocket;

	public server6(Socket clientSocket) {
		this.concurrentSocket = clientSocket;
	}

	public static void main(String[] args) {
		try {
			try (ServerSocket serverSocket = new ServerSocket(10000)) {
				System.out.println("Aguardando Cliente");
				while (true){
					Socket clientSocket = serverSocket.accept();
					System.out.println("Cliente conectado:"+clientSocket);
					server6 client = new server6(clientSocket);
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

                char nivel = dados[1].charAt(0);
                float salario = Float.parseFloat(dados[2]);
                int ndep = Integer.parseInt(dados[3]);
            
                if (nivel == 'A')
                    if (ndep > 0)
                        salario = salario * 0.97f;
                    else
                        salario = salario * 0.92f;
                else if (nivel == 'B')
                    if (ndep > 0)
                        salario = salario * 0.95f;
                    else
                        salario = salario * 0.90f;
                else if (nivel == 'C')
                    if (ndep > 0)
                        salario = salario * 0.92f;
                    else
                        salario = salario * 0.85f;
                else if (nivel == 'D')
                    if (ndep > 0)
                        salario = salario * 0.90f;
                    else
                        salario = salario * 0.83f;
            
            
                out.println(dados[0]+"_"+nivel+"_"+salario+"_"+ndep);
                System.out.println("Dados enviados ao cliente.");
			} catch (NumberFormatException e) {
			
				e.printStackTrace();
			}
		} 
        catch (IOException i){}
	}
}