import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, async_session_maker
from models import Base, Exercise, Food
from AI.workoutgenerator import EXERCISE_DB
from AI.mealplanner import FOODS

async def init_db():
    print("Creating tables in Neon DB...")
    async with engine.begin() as conn:
        # For development, you might want to drop tables first, 
        # but in production you wouldn't do this blindly.
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    print("Tables created successfully.")
    
    # Seed data
    async with async_session_maker() as session:
        # Check if exercises already exist
        from sqlalchemy import select
        result = await session.execute(select(Exercise).limit(1))
        first_ex = result.scalars().first()
        
        if not first_ex:
            print("Seeding Exercise table...")
            for ex in EXERCISE_DB:
                new_ex = Exercise(name=ex['name'], type=ex['type'], level=ex['level'])
                session.add(new_ex)
            
        result = await session.execute(select(Food).limit(1))
        first_food = result.scalars().first()
        
        if not first_food:
            print("Seeding Food table...")
            for f in FOODS:
                new_food = Food(name=f['name'], type=f['type'], category=f['category'], calories=f['calories'])
                session.add(new_food)
        
        await session.commit()
        print("Database seeding complete.")

if __name__ == "__main__":
    asyncio.run(init_db())
