import React from "react";
import {
  ComposedChart,
  Line,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

const data = [
  {
    name: "비스킷",
    fat: 4.0,
    mean: 4.76,
  },
  {
    name: "크래커",
    fat: 1.0,
    mean: 4.76,
  },
  {
    name: "채썬밀비스킷",
    fat: 1.0,
    mean: 4.76
  },
  {
    name: "와플",
    fat: 9.0,
    mean: 4.76
  },
  {
    name: "애플베티",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "빵푸딩",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "케이크",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "초콜릿퍼지",
    fat: 14.0,
    mean: 4.76
  },
  {
    name: "컵케이크",
    fat: 3.0,
    mean: 4.76
  },
  {
    name: "과일케이크",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "생강빵",
    fat: 7.0,
    mean: 4.76
  },
  {
    name: "스폰지케이크",
    fat: 2.0,
    mean: 4.76
  },
  {
    name: "사탕",
    fat: 3.0,
    mean: 4.76
  },
  {
    name: "초콜릿크림",
    fat: 4.0,
    mean: 4.76
  },
  {
    name: "퍼지",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "단단한사탕",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "마쉬멜로우",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "밀크초콜릿",
    fat: 6.0,
    mean: 4.76
  },
  {
    name: "초콜릿시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "도너츠",
    fat: 7.0,
    mean: 4.76
  },
  {
    name: "꿀",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "빙과",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "보존",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "젤리",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "당밀",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "캔디시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "9호파이",
    fat: 13.0,
    mean: 4.76
  },
  {
    name: "체리파이",
    fat: 13.0,
    mean: 4.76
  },
  {
    name: "레몬머랭",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "갈아놓은고기",
    fat: 9.0,
    mean: 4.76
  },
  {
    name: "호박파이",
    fat: 12.0,
    mean: 4.76
  },
  {
    name: "설탕3티스푼",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "시럽",
    fat: 0.0,
    mean: 4.76
  },
  {
    name: "타피오카크림푸딩",
    fat: 10.0,
    mean: 4.76
  },
];

export default function Vertical() {
  return (
    <ComposedChart
      layout="vertical"
      width={900}
      height={1000}
      data={data}
      margin={{
        top: 20,
        right: 20,
        bottom: 20,
        left: 100
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <YAxis dataKey="name" type="category" scale="band" />
      <XAxis type="number" />
      <Tooltip />
      <Legend />
      <Bar dataKey="fat" barSize={7} fill="#D62828" />
      <Line type="monotone"  dataKey="mean" stroke="#003049" />
    </ComposedChart>
  );
}
