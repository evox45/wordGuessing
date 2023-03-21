import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=evox1337")

# Open a cursor to perform database operations
cur = conn.cursor()
# try to add our table to the database
try:
    cur.execute("""

    CREATE TABLE public.words (
        id serial NOT NULL,
        word varchar NOT NULL
    );
    """)

    cur.execute("""
        ALTER TABLE public.words ADD CONSTRAINT words_pk PRIMARY KEY (id);
    """)


    # push our changes to the table
    conn.commit()

    #if it was a duplicate table error
except psycopg2.errors.DuplicateTable as e:
    print("Table already exists, ignore and adding words")
    conn.rollback()

    #if it was any other type of error
except Exception as e:
    print(" Oh no, something bad happend")
    print(e)
    exit()

# Read from the file
file = open("wordlist", "r")
allTheLinesOfTheFile = file.readlines()
file.close()

for word in allTheLinesOfTheFile:
    cur.execute("INSERT INTO public.words (word) VALUES(%s);", [word.strip()])

conn.commit()





conn.close()


