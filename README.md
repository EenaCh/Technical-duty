
Чемпионат по программированию Яндекс

Реализация большого проекта — очень сложная задача, и при разработке программист Алексей руководствуется следующим принципом: сначала написать работающий прототип, а потом улучшать код. Чтобы не забыть, что именно отложено на потом, на каждый такой долг Алексей заводит на себя задачу в специальной системе Yagile.
Система устроена следующим образом: для каждой задачи задается дедлайн — день ti. 
Если задача не решена до этого момента времени, то в задачу приходит робот и пишет комментарий о том, что задачу надобно закрыть. Если через X дней задача не решена, то робот приходит снова. Так продолжается до тех пор, пока задача не будет решена.
Алексей каждый день заходит в Yagile и видит сообщения от робота. Если Алексей не хочет приступать к решению накопленных задач, то он прочитывает все сообщения с помощью одной кнопки и занимается другими делами. Однако Алексей понимает, что так долго делать нельзя, поэтому он разрешает себе нажимать на эту кнопку ровно K−1 раз, а на K-й раз садится и решает все задачи разом (даже те, у которых не настал дедлайн).
Определите день, когда Алексей закроет все задачи.

Формат ввода

Первая строка содержит три целых числа 
N (1≤N≤10^5) — количество накопленных задач, X (1≤X≤10^9) — количество дней, через которое приходит робот и число K из условия (1≤K≤10^9).
Вторая строка содержит 
N целых чисел t1, t2, …, tN (1≤ti≤10^9) — дедлайны соответствующих задач.

Формат вывода

Выведите одно число — день, когда Алексей закроет все задачи.

Пример 1

Ввод	

6 5 10

1 2 3 4 5 6

Вывод: 10


Пример 2

Ввод	

5 7 12

5 22 17 13 8

Вывод: 27
