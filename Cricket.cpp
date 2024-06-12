#include <iostream>
#include <cstdlib>
#include <time.h>
#include <stdlib.h>
using namespace std;
class cricket
{
public:

int a,b,c,p;

int k=0;
int inst_score=0;
int total_score=0;
int comp_ent;
long final_total_score=3e7;

int comp_k=0;
int comp_inst_score=0;
int comp_total_score=0;
int ent;
int comp_final_total_score=3e7;
    

public:
void game();
void player_bat();
void result();
void computer_bat();

}; 

void cricket::game()
{
    cout<<"Heads(0) / Tails(1): "<<endl;
    cin>>a;
    if(a!=0 && a!=1)
    {
        cout<<"Get a coin"<<endl;
        exit(1);
    }
    b=rand() % 2;
    if (a==b)
    {
        cout<<"You have won the toss"<<endl;
        cout<<"Bat(1) or Bowl(0): "<<endl;
        cin>>p;
        if(p!=1 && p!=0)
        {
            cout<<"Please Exit"<<endl;
            exit(1);
        }
        if(p==1)
        {
            cout<<"You have chosen to bat first"<<endl;
            player_bat();
            final_total_score = total_score;
            cout<<"Your Score is "<<total_score<<endl;
            cout<<"Now it is the computer's turn to bat"<<endl;
            computer_bat();
            comp_final_total_score = comp_total_score;
            cout<<"Computer Score is "<<comp_total_score<<endl;
            result();
        }
        else
        {
            cout<<"You have chosen to bowl first"<<endl;
            computer_bat();
            comp_final_total_score = comp_total_score;
            cout<<"Computer Score is "<<comp_total_score<<endl;
            cout<<"Now it is your turn to bat"<<endl;
            player_bat();
            final_total_score = total_score;
            cout<<"Your Score is "<<total_score<<endl;
            result();
        }
    }
    else
    { 
        cout<<"Computer has won the toss"<<endl;
        c=rand() % 2;
        if(c==1)
        {
            cout<<"The Computer chose to Bat first"<<endl;
            computer_bat();
            comp_final_total_score = comp_total_score;
            cout<<"Computer Score is "<<comp_total_score<<endl;
            cout<<"Now it is your turn to bat"<<endl;
            player_bat();
            final_total_score = total_score;
            cout<<"Your Score is "<<total_score<<endl;
            result();
        }
        else
        {
            cout<<"The Computer chose to Bowl first"<<endl;
            player_bat();
            final_total_score = total_score;
            cout<<"Your Score is "<<total_score<<endl;
            cout<<"Now it is the computer's turn to bat"<<endl;
            computer_bat();
            comp_final_total_score = comp_total_score;
            cout<<"Computer Score is "<<comp_total_score<<endl;
            result(); 
        }
    }    
}

void cricket::result()
{
    if (total_score==comp_total_score)
        cout<<"DRAW!"<<endl;
    else if(total_score>comp_total_score)
        cout<<"YOU WIN!!"<<endl;
    else
        cout<<"YOU LOSE!!"<<endl;
}

void cricket::player_bat()
{
    
    while(k==0)
    {
        cout<<"Enter a score(1-10): "<<endl;
        cin>>inst_score;
        if (inst_score>10)
        {
            cout<<"Invalid"<<endl;
            continue;
        }
        if (inst_score<1)
        {
            cout<<"Invalid"<<endl;
            continue;
        }
        comp_ent=(rand() % 10)+1;
        if(comp_ent==inst_score)
        {
            cout<<"Crazy"<<endl;
            inst_score=comp_ent*comp_ent;
        }
        else if(comp_ent==(inst_score+1) || comp_ent==(inst_score-1))
        {
            cout<<"You are out."<<endl;
            cout<<"The Computer returned: "<<comp_ent<<endl;
            k=1;
            break;
        }
        total_score=total_score+inst_score;
        inst_score=0;
        if(total_score>comp_final_total_score)
        {
            k=1;
            break;
        }
    }
}

void cricket::computer_bat()
{
    while(comp_k==0)
    {
        cout<<"Enter a number to dismiss the computer(1-10): "<<endl;
        cin>>ent;
        if (ent>10)
        {
            cout<<"Invalid"<<endl;
            continue;
        }
        if (ent<1)
        {
            cout<<"Invalid"<<endl;
            continue;
        }
        comp_inst_score=(rand() % 10)+1;
        cout<<"The Computer returned: "<<comp_inst_score<<endl;
        if(ent==comp_inst_score)
        {
            cout<<"Crazy"<<endl;
            comp_inst_score=ent*ent;
        }
        else if(ent==(comp_inst_score+1) || ent==(comp_inst_score-1))
        {
            cout<<"The Computer is out."<<endl;
            comp_k=1;
            break;
        }
        comp_total_score=comp_total_score+comp_inst_score;
        comp_inst_score=0;
        if(comp_total_score>final_total_score)
        {
                comp_k=1;
                break;
        }
    }
}

int main()
{
    srand(time(0));
    cout<<"Welcome To Crazy Cricket."<<endl;
    cout<<"RULES: "<<endl;
    cout<<"-----"<<endl; 
    cout<<endl;
    cout<<"1) BATTING: "<<endl;
    cout<<"When you are batting per ball you can score from 1 - 10 runs, but u will be out if the computer also returns a neighbouring number which u enter."<<endl;
    cout<<endl;
    cout<<"2) BOWLING: "<<endl;
    cout<<"When you are bowling for each ball the computer will score 1 - 10 runs per ball and to dismiss it you have to enter a number neighbouring to that returned by the computer."<<endl;
    cout<<endl;
    cout<<"At the end of the game who scores the most runs in the game is the WINNER"<<endl;
    cout<<endl;
    cricket c;
    c.game();
    return 0;
}
