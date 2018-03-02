package controller;

import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        Media media = new Media();
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入名称：");
        media.setName(scanner.nextLine());
        System.out.println("请输入作者：");
        media.setAuthor(scanner.nextLine());
        System.out.println("请输入出版社：");
        media.setPublisher(scanner.nextLine());
        System.out.println("请输入价格：");
        media.setPrice(scanner.nextDouble());
        scanner.close();
    }
}
