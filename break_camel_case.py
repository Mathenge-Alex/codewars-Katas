# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    if " " in s:
        for str in s.split(" "):
            s = s[0] + s[1:].upper()
    else:
        for i in range(1, len(s)):
            lett = s[i]
            if lett.isupper():
                s = s[:i] +" " + s[i:]
    return s







# ed Tests
# Basic Test Cases
# 'hello     World' should equal 'hello World'
# 'camel    Case' should equal 'camel Case'
# 'break         CamelCase' should equal 'break Camel Case'
# Completed in 0.06ms
# Edge Test Cases
# Test Passed
# Test Passed
# 'consecutive        CApitals' should equal 'consecutive C Apitals'
# Completed in 0.05ms
# Completed in 0.15ms
# Random Tests
# s = 'leaveThink'
# 'leave     Think' should equal 'leave Think'
# Completed in 0.01ms
# s = 'pointFirstYear'
# 'point         FirstYear' should equal 'point First Year'
# Completed in 0.02ms
# s = 'badSayCompanyPointNumber'
# 'bad                     SayCompanyPointNumber' should equal 'bad Say Company Point Number'
# Completed in 0.02ms
# s = 'badTrySeem'
# 'bad       TrySeem' should equal 'bad Try Seem'
# Completed in 0.02ms
# s = 'companyTellNextVerbsBig'
# 'company                TellNextVerbsBig' should equal 'company Tell Next Verbs Big'
# Completed in 0.03ms
# s = 'caseTake'
# 'case    Take' should equal 'case Take'
# Completed in 0.01ms
# s = 'longNextLifeProblem'
# 'long               NextLifeProblem' should equal 'long Next Life Problem'
# Completed in 0.02ms
# s = 'fewGreatTakeGovernment'
# 'few                   GreatTakeGovernment' should equal 'few Great Take Government'
# Completed in 0.03ms
# s = 'adjectivesSee'
# 'adjectives   See' should equal 'adjectives See'
# Completed in 0.01ms
# s = 'tellLook'
# 'tell    Look' should equal 'tell Look'
# Completed in 0.02ms
# s = 'leaveCompanyWantNext'
# 'leave               CompanyWantNext' should equal 'leave Company Want Next'
# Completed in 0.02ms
# s = 'useAdjectives'
# 'use          Adjectives' should equal 'use Adjectives'
# Completed in 0.01ms
# s = 'takeLifeLargePart'
# 'take             LifeLargePart' should equal 'take Life Large Part'
# Completed in 0.02ms
# s = 'fewNouns'
# 'few     Nouns' should equal 'few Nouns'
# Completed in 0.01ms
# s = 'numberBadTryWork'
# 'number          BadTryWork' should equal 'number Bad Try Work'
# Completed in 0.02ms
# s = 'weekLargeAsk'
# 'week        LargeAsk' should equal 'week Large Ask'
# Completed in 0.02ms
# s = 'lifeLastDoLittle'
# 'life            LastDoLittle' should equal 'life Last Do Little'
# Completed in 0.02ms
# s = 'makeCallWork'
# 'make        CallWork' should equal 'make Call Work'
# Completed in 0.02ms
# s = 'useBePublicLookMake'
# 'use                BePublicLookMake' should equal 'use Be Public Look Make'
# Completed in 0.02ms
# s = 'weekFeel'
# 'week    Feel' should equal 'week Feel'
# Completed in 0.01ms
# s = 'rightEyeLarge'
# 'right        EyeLarge' should equal 'right Eye Large'
# Completed in 0.02ms
# s = 'childSeemPartLook'
# 'child            SeemPartLook' should equal 'child Seem Part Look'
# Completed in 0.02ms
# s = 'governmentAsk'
# 'government   Ask' should equal 'government Ask'
# Completed in 0.02ms
# s = 'seeEarly'
# 'see     Early' should equal 'see Early'
# Completed in 0.01ms
# s = 'numberNumberFewFeel'
# 'number             NumberFewFeel' should equal 'number Number Few Feel'
# Completed in 0.02ms
# s = 'sayBadFewSeem'
# 'say          BadFewSeem' should equal 'say Bad Few Seem'
# Completed in 0.02ms
# s = 'getOwnHaveThinkHand'
# 'get                OwnHaveThinkHand' should equal 'get Own Have Think Hand'
# Completed in 0.02ms
# s = 'personEarlyNext'
# 'person         EarlyNext' should equal 'person Early Next'
# Completed in 0.02ms
# s = 'companyTimeGetKnowLittle'
# 'company                 TimeGetKnowLittle' should equal 'company Time Get Know Little'
# Completed in 0.03ms
# s = 'askPublicOldDoLeave'
# 'ask                PublicOldDoLeave' should equal 'ask Public Old Do Leave'
# Completed in 0.02ms
# s = 'workPointChild'
# 'work          PointChild' should equal 'work Point Child'
# Completed in 0.02ms
# s = 'lastPlaceImportant'
# 'last              PlaceImportant' should equal 'last Place Important'
# Completed in 0.02ms
# s = 'placeBig'
# 'place   Big' should equal 'place Big'
# Completed in 0.01ms
# s = 'seeDay'
# 'see   Day' should equal 'see Day'
# Completed in 0.01ms
# s = 'bigKnowGroup'
# 'big         KnowGroup' should equal 'big Know Group'
# Completed in 0.01ms
# s = 'thingKnowAble'
# 'thing        KnowAble' should equal 'thing Know Able'
# Completed in 0.02ms
# s = 'worldLittleLeaveSmall'
# 'world                LittleLeaveSmall' should equal 'world Little Leave Small'
# Completed in 0.03ms
# s = 'numberDayEarlyLookDo'
# 'number              DayEarlyLookDo' should equal 'number Day Early Look Do'
# Completed in 0.02ms
# s = 'largeLeaveTake'
# 'large         LeaveTake' should equal 'large Leave Take'
# Completed in 0.02ms
# s = 'leaveLongDifferentNextYoung'
# 'leave                      LongDifferentNextYoung' should equal 'leave Long Different Next Young'
# Completed in 0.03ms
# s = 'earlyUse'
# 'early   Use' should equal 'early Use'
# Completed in 0.02ms
# s = 'feelOwnOtherDo'
# 'feel          OwnOtherDo' should equal 'feel Own Other Do'
# Completed in 0.02ms
# s = 'callNext'
# 'call    Next' should equal 'call Next'
# Completed in 0.01ms
# s = 'manGovernmentAskPlace'
# 'man                  GovernmentAskPlace' should equal 'man Government Ask Place'
# Completed in 0.03ms
# s = 'seemPointWomanHave'
# 'seem              PointWomanHave' should equal 'seem Point Woman Have'
# Completed in 0.02ms
# s = 'useFirstBe'
# 'use       FirstBe' should equal 'use First Be'
# Completed in 0.01ms
# s = 'newGet'
# 'new   Get' should equal 'new Get'
# Completed in 0.01ms
# s = 'thingMakeTryCome'
# 'thing           MakeTryCome' should equal 'thing Make Try Come'
# Completed in 0.02ms
# s = 'timeUseLook'
# 'time       UseLook' should equal 'time Use Look'
# Completed in 0.02ms
# s = 'thingTell'
# 'thing    Tell' should equal 'thing Tell'
# Completed in 0.01ms
# Completed in 5.30ms








print(sorted([3,5,8,2,5,1,8,0,5,8,4]))







