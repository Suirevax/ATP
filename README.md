# ATP
## Decorator
Wordt toegepast in `main.py` Voor het toevoegen van logging aan de `GroundHumiditySensor` zonder effect van functie aan te passen.

## Unit-test
Er is een unit-test geschreven voor de helper functie `normalize` in de file `HelperfunctionsUnitTest.py`. Deze test is uit te voeren door deze file uit te voeren.
Resultaat: 
```
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## Integratie test
Er is een integratie test geschreven om de koppeling functie tussen de grond vochtigheids sensor en actuator te controleren. Deze test bevindt zich in `HumidityControllerIntegrationtest.py`.
Resultaat:
```
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

## Systeem test
De syteem test vervangt de sensoren functies met functies die willekeurige getallen genereren. De Actuator functie wordt vervangen met functies die alleen hun ontvangen waarde loggen.
De systeem test is uit te voeren door deze aan te zetten in `main.py` (regel 25).
Resultaat:
```
Prepare systemtest
Update
GetHumiditySensor Return value: 760
GroundHumidityActuatorAction: 190.4
GetLightSensor Return value: 63667
LightIntensityActuatorAction: 247.73140659810176
Update
GetHumiditySensor Return value: 2383
GroundHumidityActuatorAction: 52.445
GetLightSensor Return value: 27454
LightIntensityActuatorAction: 106.82264168218025
Update
GetHumiditySensor Return value: 1755
GroundHumidityActuatorAction: 105.825
GetLightSensor Return value: 64764
LightIntensityActuatorAction: 251.99995422223577
Update
GetHumiditySensor Return value: 2529
GroundHumidityActuatorAction: 40.035
GetLightSensor Return value: 34629
LightIntensityActuatorAction: 134.74135563219093
...
```

## C Binding
De C binding is te vinden in `GroundHumidityActuator.py`. Deze vormt een binding met arduino.so om de functionaliteit van de servo motor te implementeren.

# Testplan afwijking
Uiteindelijk ben ik redelijk wat afgeweken van het originele plan. Ik heb geen classes gebruikt en geen Interfaces geimplementeerd. De reden hiervoor was simpel weg vermindering van onnodige complexiteit. Wel is alsnog sterk de focus gelegd op de grond vochtigheids regel functionaliteit van het systeem vanwege de ernstigere schade die het aan kan richten in het geval van verkeerd gedrag.