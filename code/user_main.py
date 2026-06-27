# Zebra Example: Ackermann Drive
# Runs one drive motor and one steering servo, then centers and stops.

import uasyncio as asyncio
from robot.ackermann import AckermannDrive


async def main(zbot):
    drive = AckermannDrive(
        zbot,
        drive_motor_port=3,
        steering_port=2,
        center_angle=90,
        min_angle=45,
        max_angle=135,
    )
 
    zbot.display("Ackermann", "Forward")
    drive.drive(-40, 90)
    await asyncio.sleep_ms(1200)

    zbot.display("Ackermann", "square")
    drive.drive(-90, 90)
    await asyncio.sleep_ms(5500)
   
    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)
  
    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)

    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)
    
    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)
  
    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)
  
    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)
    
    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)

    zbot.display("Ackermann", "Stopped")
    drive.stop()
    drive.steer_center()

    while True:
        await asyncio.sleep_ms(1000)