from string import Template

ORDER_PLACED_TEMPLATE = Template("Order Placed:\nBOT:   $botId\n Symbol:    $symbol\n$side @$price qty:$qty")
ORDER_CANCELLED_TEMPLATE = Template("Order Cancelled:\nBOT: $botId\n Symbol: $symbol\n$side @$price qty:$qty\nfilled: $filled\nCreated @$t1 Cancelled @$t2")
ORDER_FILLED_TEMPLATE = Template("Order Filled:\nBOT:   $botId\n Symbol:    $symbol\n$side @$price qty:$qty\nfilled: $filled\nCreated @$t1 TimeNow @$t2")

RANDOM = [
    "I'm not going there to die. I'm going there to find out if I'm really alive.",
    "The only difference between a hero and a madman is whether they win or lose",
    "The Internet: transforming society and shaping the future through chat.",
    "Computer Science is no more about computers than astronomy is about telescopes.",
    "Computers are good at following instructions, but not at reading your mind.",
    "Luck is what happens when preparation meets opportunity.",
    "Through action, a man becomes a Hero.\nThrough death, the Hero becomes a Legend.\nThrough time, the Legend becomes a Myth.\nAnd by learning from the myth, a man takes action.",
    "In a few hours, the sun will rise!",
    "He who will not economize will have to agonize."
]

FIGHT = [
    "Baka!",
    "Piss Off.",
    "Dafuq Mate.",
    "Stop Bothering Me.",
    "I can see your browser history.",
    "If you are reading this you may celebrate wasting 5 seconds of your life."
]


PASS = [
    Template("You may pass $name!"),
    Template("You are in the know $name!"),
    Template("Ka-Ching $name!"),
    Template("Youre cool $name!")
]
