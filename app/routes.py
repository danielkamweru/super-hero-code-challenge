from flask import jsonify, request
from flask_mail import Message
from app.models import Hero, Power, HeroPower
from app import db, mail


def register_routes(app):

    
    # HERO POWERS
    
    @app.post('/hero_powers')
    def create_hero_power():
        try:
            data = request.get_json()

            hero = Hero.query.get(data['hero_id'])
            power = Power.query.get(data['power_id'])

            if not hero or not power:
                return jsonify({
                    "errors": ["Hero or Power not found"]
                }), 404

            hp = HeroPower(
                strength=data['strength'],
                hero_id=hero.id,
                power_id=power.id
            )

            db.session.add(hp)
            db.session.commit()

            # Send email notification
            try:
                msg = Message(
                    subject=f"New Hero-Power Association: {hero.super_name} + {power.name}",
                    recipients=['kamwerudaniel5@gmail.com'],  # Send to user's email
                    body=f"A new hero-power association has been created:\n\nHero: {hero.super_name} ({hero.name})\nPower: {power.name}\nStrength: {hp.strength}"
                )
                mail.send(msg)
            except Exception as e:
                # Log email error but don't fail the request
                print(f"Email sending failed: {e}")

            return jsonify({
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "hero": hero.to_dict(),
                "power": power.to_dict()
            }), 201

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 422


    @app.delete('/hero_powers/<int:id>')
    def delete_hero_power(id):
        hp = HeroPower.query.get(id)
        if not hp:
            return jsonify({"error": "Hero power not found"}), 404

        db.session.delete(hp)
        db.session.commit()
        return jsonify({"message": "Hero power deleted successfully"}), 200
    # HEROES
    
    @app.get('/heroes')
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([h.to_dict() for h in heroes]), 200


    @app.get('/heroes/<int:id>')
    def get_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "strength": hp.strength,
                    "power": hp.power.to_dict()
                } for hp in hero.hero_powers
            ]
        }), 200


    @app.post('/heroes')
    def create_hero():
        try:
            data = request.get_json()

            hero = Hero(
                name=data['name'],
                super_name=data['super_name']
            )

            db.session.add(hero)
            db.session.commit()

            return jsonify(hero.to_dict()), 201

        except KeyError:
            return jsonify({
                "errors": ["name and super_name are required"]
            }), 422


    @app.delete('/heroes/<int:id>')
    def delete_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        db.session.delete(hero)
        db.session.commit()
        return jsonify({"message": "Hero deleted successfully"}), 200


    # POWERS
    
    @app.get('/powers')
    def get_powers():
        powers = Power.query.all()
        return jsonify([p.to_dict() for p in powers]), 200


    @app.get('/powers/<int:id>')
    def get_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        return jsonify(power.to_dict()), 200


    @app.post('/powers')
    def create_power():
        try:
            data = request.get_json()

            power = Power(
                name=data['name'],
                description=data['description']
            )

            db.session.add(power)
            db.session.commit()

            return jsonify(power.to_dict()), 201

        except KeyError:
            return jsonify({
                "errors": ["name and description are required"]
            }), 422


    @app.patch('/powers/<int:id>')
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404

        try:
            power.description = request.json.get("description")
            db.session.commit()
            return jsonify(power.to_dict()), 200
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 422


    @app.delete('/powers/<int:id>')
    def delete_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404

        db.session.delete(power)
        db.session.commit()
        return jsonify({"message": "Power deleted successfully"}), 200


