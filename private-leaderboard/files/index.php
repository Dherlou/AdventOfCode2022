<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AdventOfCode - RZ Leaderboard</title>
    <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
</head>
<body>
    <?php
        $aoc_cookie = getenv('AOC_SESSION_COOKIE');
        $aoc_data = json_decode(file_get_contents("data.json"), true);
        echo("<pre>" . json_encode($aoc_data, JSON_PRETTY_PRINT) . "<pre/>");
    ?>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
<script src="bootstrap.min.js"></script>
</body>
</html>