import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) {
        try {
            int r = 12, g = 13, b = 14;
            int res = 0;

            File input_file = new File("input.txt");
            Scanner reader = new Scanner(input_file);

            while (reader.hasNextLine()) {
                String s = reader.nextLine();
                s = s.replace("\n", "");
                String[] n_games = s.split(": ");

                Integer n = Integer.parseInt(n_games[0].replace("Game ", ""));
                Boolean valid_game = true;

                String games_str = n_games[1];
                for (String game : games_str.split("; ")) {
                    for (String color : game.split(", ")) {
                        if (color.endsWith(" red") & (Integer.parseInt(color.split(" ")[0]) > r)) {
                            valid_game = false;
                        } else if (color.endsWith(" green") & (Integer.parseInt(color.split(" ")[0]) > g)) {
                            valid_game = false;
                        } else if (color.endsWith(" blue") & (Integer.parseInt(color.split(" ")[0]) > b)) {
                            valid_game = false;
                        }
                    }
                }
                if (valid_game) {
                    res += n;
                }
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
