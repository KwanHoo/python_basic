import React from "react";
import {
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  ZAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  LabelList
} from "recharts";

const data01 = [
  { x: 8, y: 5,  z: 190, n: '콩 수프' },
  { x: 6, y: 4, z: 100, n: '쇠고기 수프' },
  { x: 4, y: 2, z: 75, n: '치킨 수프' },
  { x: 7, y: 12, z: 200, n: '크림 수프' },
  { x: 6, y: 7, z: 175, n: '토마토 수프' },
  { x: 4, y: 2, z: 80, n: '채소 수프' }
];

const data02 = [
  {
    n: "비스킷",
    y: 4.0,
    x: 3, z: 130,
  },
  {
    n: "크래커",
    y: 1.0,
    x:1 , z: 15,
  },  {
    n: "채썬 밀 비스킷",
    y: 1.0,
    x: 3, z:100,
  },
  {
    n: "와플",
    y: 9.0,
    x: 8, z: 240
  },
  {
    n: "애플 베티",
    y: 4.0,
    x: 1, z: 150
  },
  {
    n: "빵 푸딩",
    y: 12.0,
    x: 11, z:374
  },
  {
    n: "케이크",
    y: 0.0,
    x: 3, z:110
  },
  {
    n: "초콜릿 퍼지",
    y: 14.0,
    x: 5, z:420
  },
  {
    n: "컵 케이크",
    y: 3.0,
    x: 3, z:160
  },
  {
    n: "과일 케이크",
    y: 4.0,
    x: 2, z:105
  },
  {
    n: "생강 빵",
    y: 7.0,
    x: 2, z:180
  },
  {
    n: "스폰지 케이크",
    y: 2.0,
    x: 3, z:115
  },
  {
    n: "사탕",
    y: 3.0,
    x: 0, z:104
  },
  {
    n: "초콜릿 크림",
    y: 4.0,
    x: 0, z:130
  },
  {
    n: "퍼지",
    y: 12.0,
    x: 0, z:370
  },
  {
    n: "단단한 사탕",
    y: 0.0,
    x: 0, z:90
  },
  {
    n: "마쉬 멜 로우",
    y: 0.0,
    x: 1, z:98
  },
  {
    n: "밀크 초콜릿",
    y: 6.0,
    x: 2, z:290
  },
  {
    n: "초콜릿 시럽",
    y: 0.0,
    x: 0, z:80
  },
  {
    n: "도너츠",
    y: 7.0,
    x: 2, z:135
  },
  {
    n: "꿀",
    y: 0.0,
    x: 0, z:120
  },
  {
    n: "빙과",
    y: 0.0,
    x: 0, z:117
  },
  {
    n: "보존",
    y: 0.0,
    x: 0, z:55
  },
  {
    n: "젤리",
    y: 0.0,
    x: 0, z:50
  },
  {
    n: "당밀",
    y: 0.0,
    x: 0, z:45
  },
  {
    n: "캔디 시럽",
    y: 0.0,
    x: 0, z:50
  },
  {
    n: "9호 파이",
    y: 13.0,
    x: 3, z:330
  },
  {
    n: "체리 파이",
    y: 13.0,
    x: 3, z:340
  },
  {
    n: "레몬 머랭",
    y: 12.0,
    x: 4, z:300
  },
  {
    n: "갈아 놓은 고기",
    y: 9.0,
    x: 3, z:340
  },
  {
    n: "호박 파이",
    y: 12.0,
    x: 5, z:265
  },
  {
    n: "설탕 3 티스푼",
    y: 0.0,
    x: 0, z:50
  },
  {
    n: "시럽",
    y: 0.0,
    x: 0, z:100
  },
  {
    n: "타피오카 크림 푸딩",
    y: 10.0,
    x: 10, z:335
  },

];



export default function FatProtein() {
  return (
    <ScatterChart
      width={1000}
      height={400}
      margin={{
        top: 20,
        right: 20,
        bottom: 40,
        left: 20
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis type="number" dataKey="x" name="protein" unit="g"  label={{ value: "protein/g", position: "insideBottomRight" }} />
      <YAxis type="number" dataKey="y" name="fat" unit="g"  label={{ value: "fat/g", angle: -90, position: "insideLeft" }} />
      <ZAxis
        type="number"
        dataKey="z"
        range={[60, 400]}
        name="calories"
        unit="g"
      />

      <Tooltip cursor={{ strokeDasharray: "3 3" }} />
      <Legend />
      <Scatter name="Soups" data={data01} fill="#8884d8" shape="circle">
          <LabelList dataKey="n" />
      </Scatter>
      <Scatter name="Desserts" data={data02} fill="#FCBF49" shape="circle" />

    </ScatterChart>
  );
}
