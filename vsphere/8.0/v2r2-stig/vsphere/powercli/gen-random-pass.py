import random

words = [
    # NATO phonetic
    "alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel",
    "india","juliet","kilo","lima","mike","november","oscar","papa",
    "quebec","romeo","sierra","tango","uniform","victor","whiskey",
    "xray","yankee","zulu",

    # Tech / infrastructure
    "cloud","secure","kernel","docker","server","cipher","vault",
    "linux","openshift","kube","esxi","vmware","ansible","terraform",
    "gitlab","github","cluster","python","golang","powershell",
    "firewall","router","switch","storage","backup","compute",
    "virtual","container","podman","network","monitor","splunk",
    "elastic","syslog","netapp","ceph","trident","operator",
    "automation","pipeline","runner","orchestrator","platform",
    "compliance","stig","audit","crypto","token","identity",
    "gateway","proxy","console","dashboard","hypervisor","datastore",
    "firmware","driver","clustered","replica","namespace","ingress",
    "egress","policy","scanner","telemetry","metrics","logging",

    # Food / fun
    "kimchi","mandoo","bulgogi","ramen","gimbap","mandu","jjigae",
    "pajeon","bibim","soju","banchan","dumpling","noodle","burger",
    "taco","pizza","coffee","espresso","latte","cheese","bacon",
    "pepper","garlic","onion","potato","pickle","waffle","pancake",
    "cookie","brownie","churro","salsa","nacho","burrito","steak",
    "shrimp","salmon","sushi","udon","tempura","teriyaki",

    # Nature / weather
    "river","forest","mountain","ocean","desert","thunder","lightning",
    "storm","rain","snow","sunset","sunrise","shadow","ember",
    "glacier","volcano","canyon","breeze","tornado","horizon",
    "comet","meteor","galaxy","orbit","lunar","solar","planet",
    "saturn","jupiter","nebula","cosmos","aurora","starlight",

    # Fantasy / gaming / playful
    "ninja","wizard","samurai","pirate","dragon","phoenix","viking",
    "knight","ranger","hunter","mage","warlock","paladin","rogue",
    "sonic","yoda","pikachu","zelda","mario","luigi","kirby",
    "bowser","ganon","triforce","metroid","doomguy","masterchief",
    "cortana","kratos","arthur","merlin","odin","thor","loki",

    # Random human-friendly
    "buddy","sunny","happy","rocket","turbo","spark","pixel","cobalt",
    "ember","frost","copper","silver","golden","crimson","violet",
    "indigo","hazel","maple","cedar","willow","acorn","falcon",
    "eagle","wolf","otter","badger","panther","tiger","koala",
    "penguin","alpaca","lemur","gecko","moose","buffalo","yak"
]

SEPARATORS = ["-", "_", ".", "@"]

def generate_passphrase(length=15):

    while True:

        # Pick 2 short words
        word1, word2 = random.sample(words, 2)
        word1 = word1.capitalize()
        separator = random.choice(SEPARATORS)
        number = str(random.randint(10, 999))
        base = f"{word1}{separator}{word2}{separator}{number}"

        # Trim if too long
        if len(base) > length:
            continue

        # Add random chars if needed
        remaining = length - len(base)
        extra_chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz346789!@#$%"
        extra = ''.join(random.choices(extra_chars, k=remaining))
        password = base + extra

        # Shuffle tail slightly while keeping readability
        password_list = list(password)

        # Validate requirements
        if (
            len(password) == length and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%_-." for c in password)
        ):
            return password

# Generate 20 passwords
for _ in range(20):
    print(generate_passphrase())
