#RPG turn based battle
class Turn_Battle():
    #Start up
    def __init__(self):
        print("You've been drawn into battle!")
        choice=int(input("Would you like to fight? '1':Yes, '2':No-> "))
        if choice==1:
            self.battlecore(30,14,3,30,14,3)
        elif choice==2:
            print("You ran away!")
            exit()
        elif choice==3:
            print("Opening developer mode.")
            self.stat_entry()
        else:
            print("What?")
            self.__init__()
    #Value Entry
    def stat_entry(self):
        print("Welcome to developer mode. Please enter stats for this battle.")
        pc_HP_max=int(input("Player character's max HP: "))
        cpu_HP_max=int(input("Computer character's max HP: "))
        pc_MP_max=int(input("Player character's max MP: "))
        cpu_MP_max=int(input("Computer character's max MP: "))
        pc_attack=int(input("Player character's base attack: "))
        cpu_attack=int(input("Computer character's base attack: "))
        print("Starting battle.")
        self.battlecore(pc_HP_max,pc_MP_max,pc_attack,cpu_HP_max,cpu_MP_max,cpu_attack)
    #Core battle system
    def battlecore(self,pc_HP_max,pc_MP_max,pc_attack,cpu_HP_max,cpu_MP_max,cpu_attack):
        pc_HP=pc_HP_max
        pc_MP=pc_MP_max
        cpu_HP=cpu_HP_max
        cpu_MP=cpu_MP_max
        while pc_HP>0 and cpu_HP>0:
            self.graphics(pc_HP,pc_MP,pc_attack,cpu_HP,cpu_MP,cpu_attack)
            print("1:Attack 2:Magic 3:Item")
            choice=int(input("-> "))
            if choice==1:
                cpu_HP-=pc_attack
                print("You hit the monster!")
            elif choice==2:
                print("1:Fira (2MP) 2:Cura (4MP)")
                m_choice=int(input("-> "))
                if m_choice==1:
                    if pc_MP>=2:
                        print("You've used Fira!")
                        pc_MP-=2
                        cpu_HP-=(2*pc_attack)
                    else:
                        print("You don't have enough MP.")
                elif m_choice==2:
                    if pc_MP>=4:
                        print("You've used Cura.")
                        pc_MP-=4
                        pc_HP+=10
                        if pc_HP>pc_HP_max:
                            pc_HP=pc_HP_max
                    else:
                        print("You don't have enough MP.")
                else:
                    "What?"
            elif choice==3:
                print("1:Potion")
                i_choice=int(input("-> "))
                if i_choice==1:
                    print("You used a potion.")
                    pc_HP+=4
                else:
                    print("What?")
            else:
                print("What?")
            if cpu_HP>0:
                notice=int(input("It is now the enemy turn. Please press 1."))
                from random import randint
                cpu_choice=randint(1,4)
                print(cpu_choice)
                if cpu_choice<4:
                    print("The monster hit you!")
                    pc_HP-=cpu_attack
                elif cpu_choice==4:
                    cpu_choice_m=randint(1,3)
                    if cpu_choice_m<=2:
                        if cpu_MP>=2:
                            print("The monster used Fira! ")
                            cpu_MP-=2
                            pc_HP-=(2*cpu_attack)
                        elif cpu_choice_m==3:
                            if cpu_MP>=4:
                                print("The monster used Cura.")
                                cpu_MP-=4
                                cpu_HP+=10
                                if cpu_HP>cpu_HP_max:
                                    cpu_HP=cpu_HP_max
        if cpu_HP==0:
            print("You've defeated the monster!")
        elif pc_HP==0:
            print("You have been defeated.")
    #Core graphic system
    def graphics(self,pc_HP,pc_MP,pc_attack,cpu_HP,cpu_MP,cpu_attack):
        print("Monster:")
        cpu_healthbar="".join(["|"]*cpu_HP)
        print("HP: "+cpu_healthbar+" "+str(cpu_HP))
        cpu_manabar="".join(["|"]*cpu_MP)
        #print("MP: "+cpu_manabar+" "+str(cpu_MP))
        #print("Base Attack: "+str(cpu_attack)) Don't print these- player doesn't need to know monster stats
        print("\n        /-/--\ ")
        print("      (@~@)   )/\ ")
        print("  ___/--      \  |")
        print(" (oo)__ _      )_/")
        print("  ^^___/       \   ")
        print("        \       |/-\  ")
        print("         (      )   |")
        print("         |       \_/  ")
        print("\n\nPlayer Character Stats:")
        pc_healthbar="".join(["|"]*pc_HP)
        pc_manabar="".join(["|"]*pc_MP)
        print("HP: "+pc_healthbar+" "+str(pc_HP))
        print("MP: "+pc_manabar+" "+str(pc_MP))
        print("Base attack: "+str(pc_attack))
game = Turn_Battle()