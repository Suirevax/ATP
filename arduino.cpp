#include <iostream>

void analogWrite(int value){
    std::cout << "Setting PWM to:" << value << std::endl;
}

void pwm_write(int value){
    analogWrite(value);
}

int main(){
    std::cout <<"test";
}