"""
Simple seed script to populate the superheroes database with sample data.

Run with:
    python seed.py
"""

from app import create_app, db
from app.models import Hero, Power, HeroPower


def clear_data() -> None:
    """Remove existing rows so seeding is repeatable."""
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()
    db.session.commit()


def seed_data() -> None:
    # Create powers
    flight = Power(
        name="Flight",
        description="Gives the hero the ability to fly at incredible speeds.",
    )
    strength = Power(
        name="Super Strength",
        description="Allows the hero to lift and move extremely heavy objects.",
    )
    invisibility = Power(
        name="Invisibility",
        description="Lets the hero become invisible to the naked eye.",
    )

    db.session.add_all([flight, strength, invisibility])
    db.session.flush()  # Assign IDs before creating HeroPower rows

    # Create heroes
    clark = Hero(name="Clark Kent", super_name="Superman")
    diana = Hero(name="Diana Prince", super_name="Wonder Woman")
    susan = Hero(name="Susan Storm", super_name="Invisible Woman")

    db.session.add_all([clark, diana, susan])
    db.session.flush()

    # Link heroes to powers
    hero_powers = [
        HeroPower(hero_id=clark.id, power_id=flight.id, strength="Strong"),
        HeroPower(hero_id=clark.id, power_id=strength.id, strength="Strong"),
        HeroPower(hero_id=diana.id, power_id=strength.id, strength="Strong"),
        HeroPower(hero_id=susan.id, power_id=invisibility.id, strength="Average"),
    ]

    db.session.add_all(hero_powers)
    db.session.commit()


def main() -> None:
    app = create_app()
    with app.app_context():
        clear_data()
        seed_data()
        print("Database seeded successfully.")


if __name__ == "__main__":
    main()




