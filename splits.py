custom_splits = {
    "3": {
        "3 Day Push/Pull/Leg split": {
            "Day 1 - push (chest, shoulder, trap, triceps)": [
            ["BB Bench press | 10x3"],
            ["Incline db bench press | 1ox3"],
            ["DB Fly | 12x3"],
            ["Seated shoulder press | 12x3"],
            ["Upright db row | 10x3"],
            ["DB Lateral raise | 8x3"],
            ["BB Shrug | 12x3"],
            ["DB Overhead tricep extensions | 8x3"],
            ["Triceps pushdown | 8x3"]
        ],
        "Day 2 - Leg (quad, hamstring, glute, calves)": [
            ["Leg extensions 12x4"],
            ["Leg press | 10x3"],
            ["DB lunge | 12x3"],
            ["BB RDL | 10x3"],
            ["Hamstring curl machine | 10x4"],
            ["Abduction machine | 12x4"],
            ["Cable kickback | 20x3"],
            ["Standing calve machine | 30x3"]
        ],
        "Day 3 - pull (back, biceps, abs)": [
            ["Lat pull down | 12x3"],
            ["Row machine | 12x3"],
            ["Incline db row | 10x3"],
            ["Bent over db rear delt fly | 12x3"],
            ["BB Bicep curl | 10x3"],
            ["DB Hammer curl | 12x3"],
            ["DB wrist curls | 10x3"],
            ["Crunch machine | 8x3"],
            ["Hanging leg raise| 8x3"],
            ["Mountain climbers 12x3"]
        ]
        }
    },

    "4": {"4 Day Upper Lower (pull/leg(q)/push/leg(h) Custom1)": {
        "Day 1 - Upper (Back, Triceps)": [
            ["lat pulldown | 12x4"], # Back_compound
            ["BB Rows | 12 + 10 + 10 + 8"], # Back_compound
            ["H Machine | 12x4", "Single arm cable rows | 12x4"], # Back_compound/isolation
            ["DB Rows | 12x4"], # Back_isolation
            ["Straight arms | 12x3"], # Back_isolation
            ["hyperextensions | 20x4"], # Back_isolation
            ["Cable triceps pulldown | 12x3"], # Tricep_isolation
            ["DB tricep kickbacks | 8x4"] # Tricep_isolation
        ],
        "Day 2 - Lower (Quad, abductor, calve)": [
            ["Leg extensions 4x12"], # Quad_isolation
            ["Smith squats | 12 + 10 + 10 + 8"], # Quad_compound
            ["Smith lunge | 12x4", "Sumo squats | 12x4"], # Quad_compound/isolation
            ["Single leg leg press (12 + 20(both))x4", "Goblet squats | 16x4"], # Quad_compound/isolation
            ["Leg abduction machine | 16x4"], # Abductor_isolation
            ["Cable(Knee bent) kick backs | 12x4"], # Glute_isolation
            ["Standing calves machine | 20x3"], # Calves_isolation
            ["Seated calves | 30x3"] # Calves_isolation
        ],
        "Day 3 - Upper (Shoulder, Chest, Bicep)": [
            ["Smith shoulder press | 12x4", "Seated db shoulder press | 12x4"], # Shoulder_compound
            ["Cable lateral raises | 12x4"], # Shoulder_isolation
            ["DB Lateral raises | 10x4"], # Shoulder_isolation
            ["DB Front raise | 12x4"], # Shoulder_isolation
            ["Reversed fly machine | 10x3"], # Shoulder_isolation
            ["Cable rear delt | 12x4"], # Shoulder_isolation
            ["DB Chest press | 10x3"], # Chest_compound
            ["DB chest fly | 8x3"], # Chest_isolation
            ["BB Bicep curls | 8x3"], # Bicep_isolation
            ["DB hammer curls 12x3"] # Bicep_isolation
        ],
        "Day 4 - Lower (hamstring, glute)": [
            ["Hamstring curls | 12x4"], # Hamstring_isolation
            ["BB RDL | 12x4"], # Hmastring_compound
            ["BB hip thrusts | 12x4", "Cable side kick | 15x3"], # Glute_compound
            ["Bulgarian split squats | 8x3"], # Glute_isolation
            ["abduction machine | 15x4"], # OuterTighs_isolation
            ["DB lifts | 12x3"], # Glute_compound
            ["DB Step ups | 12x4"], # Glute_compound
            ["Standing calves | 30x3"] # Calve_isolation
        ]},
    },

    "5": {
        "5 Day Split (custom1)": {
            "Day1": [
                ["Smith squats (wide stance) | 12x4"], # Quad_compound
                     ["Sumo wide stance db lifts | 20x4"], # Quad_compound
                     ["RDL | 20x3"], # Hamstring_compound
                     ["Lying hamstring curls | 12x3"], # Hamstring_isolation
                     ["BB Hip thrust | 12x4"], # Glute_compound
                     ["Glute bridge (BB) | 15x4"], # Glute_compound
                     ["Standing cable hamstring curl | 15x4"], # Hamstring_isolation
                     ["Smith calf raises | 25x4"] # Calve_isolation
                     ], 
              
            "Day2": [
                ["Lat pull down (wide grip) | 12x4"], # Back_compound
                     ["Row machine | 20x4"], # Back_compound
                     ["Face pull | 12x3"], # Trap_isolation
                     ["Straight arm | 12x3"], # Lat_isolation
                     ["DB Fly back | 12x4"], # ReaeDelt_isolation
                     ["DB Lateral raises | 15x4"], # Shoulder_isolation
                     ["BB Shoulder press | 15x4"], # Shoulder_compound
                     ["Seated lateral raises | 12x4"], # Shoulder_isolation
                     ["Seated rear delt fly | 15x4"] # Shoulder_idolation
            ],
            "Day3": [
                ["Single leg leg extension 12 + both 20 | x4"], # Quad_isolation
                     ["Concentration db lifts | 20x4"], # Quad_compound
                     ["Smith squats | 12x4"], # Quad_compound
                     ["Leg press (narrow) | 12x4"], # Quad_compound
                     ["DB Lunge | 12x4"], # Quad_compound
                     ["Cable side leg raise | 15x4"], # Abductor_isolation
                     ["Standing calve raise machine | 25x4"], # Calve_isolation
                     ["Seated db calves | 25x4"] # Calve_isolation
            ],
            "Day4": [
                ["Lat pull down (wide grip) | 12x4"], # Back_compound
                     ["Row machine | 20x4"], # Back_compound
                     ["Face pull | 12x3"], # Trap_isolation
                     ["Straight arm | 12x3"], # Lat_isolation
                     ["DB Fly back | 12x4"], # ReaeDelt_isolation
                     ["DB Lateral raises | 15x4"], # Shoulder_isolation
                     ["BB Shoulder press | 15x4"], # Shoulder_compound
                     ["Seated lateral raises | 12x4"], # Shoulder_isolation
                     ["Seated rear delt fly | 15x4"] # Shoulder_idolation
            ],
            "Day5": [["Cable kick back | 12x4"], # Glute_isolation
                     ["DB Single leg hip thrusts | 20x4"], # Glute_compound
                     ["Hip thusts (BB) | 12x4"], # Glute_compound
                     ["BB RDL | 12x4"], # Hamstring_compound
                     ["DB Squats (leaning forward) | 12x4"], # Glute_compound
                     ["Abduction machine | 25x4"], # Glute_isolation
                     ["Standing straight leg kick backs (short stance) | 20x4"], # Glute_isolation
                     ["Smith calf raises | 25x4"] # Calve_isolation 
                     ]
        }
    },

    "6": {
        "6 Days Split (custom1)": {
             "Day1": [
                ["Smith squats (wide stance) | 12x4"], # Quad_compound
                     ["Sumo wide stance db lifts | 20x4"], # Quad_compound
                     ["RDL | 20x3"], # Hamstring_compound
                     ["Lying hamstring curls | 12x3"], # Hamstring_isolation
                     ["BB Hip thrust | 12x4"], # Glute_compound
                     ["Glute bridge (BB) | 15x4"], # Glute_compound
                     ["Standing cable hamstring curl | 15x4"], # Hamstring_isolation
                     ["Smith calf raises | 25x4"] # Calve_isolation
                     ], 
              
            "Day2": [
                ["Lat pull down (wide grip) | 12x4"], # Back_compound
                     ["Row machine | 20x4"], # Back_compound
                     ["Face pull | 12x3"], # Trap_isolation
                     ["Straight arm | 12x3"], # Lat_isolation
                     ["DB Fly back | 12x4"], # ReaeDelt_isolation
                     ["DB Lateral raises | 15x4"], # Shoulder_isolation
                     ["BB Shoulder press | 15x4"], # Shoulder_compound
                     ["Seated lateral raises | 12x4"], # Shoulder_isolation
                     ["Seated rear delt fly | 15x4"] # Shoulder_idolation
            ],
            "Day3": [
                ["Single leg leg extension 12 + both 20 | x4"], # Quad_isolation
                     ["Concentration db lifts | 20x4"], # Quad_compound
                     ["Smith squats | 12x4"], # Quad_compound
                     ["Leg press (narrow) | 12x4"], # Quad_compound
                     ["DB Lunge | 12x4"], # Quad_compound
                     ["Cable side leg raise | 15x4"], # Abductor_isolation
                     ["Standing calve raise machine | 25x4"], # Calve_isolation
                     ["Seated db calves | 25x4"] # Calve_isolation
            ],
            "Day4": [
                ["Lat pull down (wide grip) | 12x4"], # Back_compound
                     ["Row machine | 20x4"], # Back_compound
                     ["Face pull | 12x3"], # Trap_isolation
                     ["Straight arm | 12x3"], # Lat_isolation
                     ["DB Fly back | 12x4"], # ReaeDelt_isolation
                     ["DB Lateral raises | 15x4"], # Shoulder_isolation
                     ["BB Shoulder press | 15x4"], # Shoulder_compound
                     ["Seated lateral raises | 12x4"], # Shoulder_isolation
                     ["Seated rear delt fly | 15x4"] # Shoulder_idolation
            ],
            "Day5": [["Cable kick back | 12x4"], # Glute_isolation
                     ["DB Single leg hip thrusts | 20x4"], # Glute_compound
                     ["Hip thusts (BB) | 12x4"], # Glute_compound
                     ["BB RDL | 12x4"], # Hamstring_compound
                     ["DB Squats (leaning forward) | 12x4"], # Glute_compound
                     ["Abduction machine | 25x4"], # Glute_isolation
                     ["Standing straight leg kick backs (short stance) | 20x4"], # Glute_isolation
                     ["Smith calf raises | 25x4"] # Calve_isolation 
                     ],
            "Day6": [
                ["Single leg leg extension 12 + both 20 | x4"], # Quad_isolation
                     ["Concentration db lifts | 20x4"], # Quad_compound
                     ["Smith squats | 12x4"], # Quad_compound
                     ["Leg press (narrow) | 12x4"], # Quad_compound
                     ["DB Lunge | 12x4"], # Quad_compound
                     ["Cable side leg raise | 15x4"], # Abductor_isolation
                     ["Standing calve raise machine | 25x4"], # Calve_isolation
                     ["Seated db calves | 25x4"] # Calve_isolation
            ]
        }
    }
      # more variations...
}