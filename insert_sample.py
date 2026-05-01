import sqlite3

DB_PATH = 'data/osho.db'

def insert_sample_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Sample Events
    events = [
        ('1', 'The Mustard Seed', '1974-01-01', 'Pune', 'English'),
        ('2', 'Zen: The Path of Paradox', '1977-06-10', 'Pune', 'English'),
        ('3', 'Tantra: The Supreme Understanding', '1975-02-15', 'Bombay', 'English'),
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO events (id, title, date, location, language)
        VALUES (?, ?, ?, ?, ?)
    ''', events)

    # Sample Paragraphs
    paragraphs = [
        ('1', 0, 'The mustard seed is very small, but it has a great potential.'),
        ('1', 1, 'Jesus said, the kingdom of God is like a mustard seed.'),
        ('2', 0, 'Zen is a way of life, not a philosophy.'),
        ('2', 1, 'The paradox is that you are already what you want to be.'),
        ('3', 0, 'Tantra is the science of transformation.'),
        ('3', 1, 'In Tantra, there is no condemnation, only acceptance.'),
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO paragraphs (event_id, sequence_number, content)
        VALUES (?, ?, ?)
    ''', paragraphs)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully.")

if __name__ == '__main__':
    insert_sample_data()
