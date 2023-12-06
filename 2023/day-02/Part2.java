import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part2 {
    public static void main(String[] args) {
        try {
            int res = 0;

            File input_file = new File("input.txt");
            Scanner reader = new Scanner(input_file);

            while (reader.hasNextLine()) {
                String s = reader.nextLine();
                s = s.replace("\n", "");
                String[] n_games = s.split(": ");

                String games_str = n_games[1];

                Integer max_r = Integer.MIN_VALUE, max_g = Integer.MIN_VALUE, max_b = Integer.MIN_VALUE;

                for (String game : games_str.split("; ")) {
                    for (String color : game.split(", ")) {
                        if (color.endsWith(" red")) {
                            max_r = Math.max(max_r, Integer.parseInt(color.split(" ")[0]));
                        } else if (color.endsWith(" green")) {
                            max_g = Math.max(max_g, Integer.parseInt(color.split(" ")[0]));
                        } else if (color.endsWith(" blue")) {
                            max_b = Math.max(max_b, Integer.parseInt(color.split(" ")[0]));
                        }
                    }
                }
                res += max_r * max_g * max_b;
            }

            reader.close();

            System.out.println(res);
        } catch (FileNotFoundException e) {
            System.out.println("Input file not found");
            e.printStackTrace();
            System.exit(1);
        }
    }
}
